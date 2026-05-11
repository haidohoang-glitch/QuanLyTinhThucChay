# Stored Procedure: `KiemTra_DauVao_HopDong_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-20 15:39:32.930000
- **Ngày sửa cuối**: 2017-02-20 15:52:56.517000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_Insert]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_Insert] 
	-- Add the parameters for the stored procedure here
AS
    BEGIN

        CREATE TABLE #HopDong
            (
              [HopDongID] [INT] NOT NULL ,
              [DmMaHopDongREF] [INT] NULL ,
              [TenMaHopDong] [NVARCHAR](50) NULL ,
              [So] [NVARCHAR](50) NULL ,
              [Thang] [INT] NULL ,
              [Nam] [INT] NULL ,
              [NgayKyHopDong] [DATETIME] NULL ,
              [NhanHopDong] [NVARCHAR](1000) NULL ,
              [GiaTriHopDong] [FLOAT] NULL ,
              [SoHopDong] [NVARCHAR](50) NULL ,
              [NgayChuyenHopDongChoKeToan] [DATETIME] NULL ,
              [GhiChu] [NVARCHAR](3000) NULL ,
              [NgayNhanHopDongBanCung] [DATETIME] NULL ,
              [DmKhachHangREF] [INT] NULL ,
              [TenKhachHang] [NVARCHAR](2555) NULL ,
              [DmHinhThucKhachHangREF] [INT] NULL ,
              [TenHinhThucKhachHang] [NVARCHAR](100) NULL ,
              [DmLoaiKhachHangREF] [INT] NULL ,
              [TenLoaiKhachHang] [NVARCHAR](100) NULL ,
              [SysNhanVienREF] [INT] NULL ,
              [TenDangNhap] [NVARCHAR](100) NULL ,
              [TenNhanVien] [NVARCHAR](500) NULL ,
              [NgayDanhSoHopDong] [DATETIME] NULL ,
              [NganhHang] [NVARCHAR](1000) NULL ,
              [DmNhomREF] [INT] NULL ,
              [TrangThaiHopDong] [INT] NULL ,
              [IsBanCung] [INT] NULL ,
              [CongNo] [FLOAT] NULL ,
              [GhiChuHopDong] [NVARCHAR](4000) NULL ,
              [LyDoHuyHopDong] [NVARCHAR](4000) NULL ,
              [DangSuDung] [INT] NULL ,
              [IsGiayPhep] [INT] NULL ,
              [DmPhongBanREF] [INT] NULL ,
              [TenPhongBan] [NVARCHAR](500) NULL ,
              [DmBoPhanREF] [INT] NULL ,
              [TenBoPhan] [NVARCHAR](500) NULL ,
              [DmNhomLamViecREF] [INT] NULL ,
              [TenNhom] [NVARCHAR](500) NULL ,
              [DmDiaDiemLamViecREF] [INT] NULL ,
              [TenDiaDiemLamViec] [NVARCHAR](250) NULL ,
              [ChuyenTrang] [INT] NULL ,
              [CreatedBy] [NVARCHAR](50) NULL ,
              [CreatedAt] [DATETIME] NULL ,
              [LastModifiedBy] [NVARCHAR](50) NULL ,
              [LastModifiedAt] [DATETIME] NULL ,
              [DeletedStatus] [INT] NULL ,
              [PrintStatus] [INT] NULL ,
              [RecordStatus] [INT] NULL ,
              [IsUuDai] [INT] NULL ,
              [ThanhTienThucChay] [FLOAT] NULL ,
              [ThanhTienHoaDon] [FLOAT] NULL ,
              [ThanhTienCongNo] [FLOAT] NULL ,
              [ThanhTienThanhToan] [BIGINT] NULL ,
              [NgayHuyHopDong] [DATETIME] NULL ,
              [NguoiHuyHopDong] [NVARCHAR](500) NULL ,
              [IsCalcVoucher] [INT] NULL ,
              [GiaTriDatCoc] [BIGINT] NULL ,
              [TenNhanGoc] [NVARCHAR](1000) NULL ,
              [DmNhanGocREF] [INT] NULL
            )

        DECLARE @SQL NVARCHAR(MAX) ,
            @ThoiGian DATETIME ,
            @NgayBatDau DATETIME = '2017-02-01'
        SET @NgayBatDau = ( SELECT  MAX(LastModifiedAt)
                            FROM    ABM_Data_ThucChay.dbo.HopDong
                          )

	
        SET @SQL = 'Call Kiemsoat_get_hdcn_hd ('''''
            + CONVERT(NVARCHAR(20), @NgayBatDau, 120) + ''''',' + ''''''
            + CONVERT(NVARCHAR(20), @ThoiGian, 120) + ''''');'

        SET @SQL = 'SELECT hd.HopDongID,
	hd.DmMaHopDongREF,
	hd.TenMaHopDong,
	hd.So,
	hd.Thang,
	hd.Nam,
	CONVERT(DATETIME,hd.NgayKyHopDong),
	hd.NhanHopDong,
	hd.GiaTriHopDong,
	hd.SoHopDong,
	CONVERT(DATETIME,hd.NgayChuyenHopDongChoKeToan),
	hd.GhiChu,
	CONVERT(DATETIME,hd.NgayNhanHopDongBanCung),
	hd.DmKhachHangREF,
	hd.TenKhachHang,
	hd.DmHinhThucKhachHangREF,
	hd.TenHinhThucKhachHang,
	hd.DmLoaiKhachHangREF,
	hd.TenLoaiKhachHang,
	hd.SysNhanVienREF,
	hd.TenDangNhap,
	hd.TenNhanVien,
	CONVERT(DATETIME,hd.NgayDanhSoHopDong),
	hd.NganhHang,
	hd.DmNhomREF,
	hd.TrangThaiHopDong,
	hd.IsBanCung,
	hd.CongNo,
	hd.GhiChuHopDong,
	hd.LyDoHuyHopDong,
	hd.DangSuDung,
	hd.IsGiayPhep,
	hd.DmPhongBanREF,
	hd.TenPhongBan,
	hd.DmBoPhanREF,
	hd.TenBoPhan,
	hd.DmNhomLamViecREF,
	hd.TenNhom,
	hd.DmDiaDiemLamViecREF,
	hd.TenDiaDiemLamViec,
	hd.ChuyenTrang,
	hd.CreatedBy,
	CONVERT(DATETIME,hd.CreatedAt),
	hd.LastModifiedBy,
	CONVERT(DATETIME,hd.LastModifiedAt),
	hd.DeletedStatus,
	hd.PrintStatus,
	hd.RecordStatus,
	hd.IsUuDai,
	hd.ThanhTienThucChay,
	hd.ThanhTienHoaDon,
	CONVERT(FLOAT,hd.ThanhTienCongNo),
	hd.ThanhTienThanhToan,
	CONVERT(DATETIME,hd.NgayHuyHopDong),
	hd.NguoiHuyHopDong,
	hd.IsCalcVoucher,
	hd.GiaTriDatCoc,
	hd.TenNhanGoc,
    hd.DmNhanGocREF
	from openquery(MYSQL,''' + @SQL + ''') hd
     '

        PRINT @SQL

        INSERT  INTO #HopDong
                EXECUTE ( @SQL
                       )

	--INSERT INTO [192.168.23.146].ABM_Data_ThucChay.dbo.HopDongSyn   ( HopDongID ,
	--          DmMaHopDongREF ,
	--          TenMaHopDong ,
	--          So ,
	--          Thang ,
	--          Nam ,
	--          NgayKyHopDong ,
	--          NhanHopDong ,
	--          GiaTriHopDong ,
	--          SoHopDong ,
	--          NgayChuyenHopDongChoKeToan ,
	--          GhiChu ,
	--          NgayNhanHopDongBanCung ,
	--          DmKhachHangREF ,
	--          TenKhachHang ,
	--          DmHinhThucKhachHangREF ,
	--          TenHinhThucKhachHang ,
	--          DmLoaiKhachHangREF ,
	--          TenLoaiKhachHang ,
	--          SysNhanVienREF ,
	--          TenDangNhap ,
	--          TenNhanVien ,
	--          NgayDanhSoHopDong ,
	--          NganhHang ,
	--          DmNhomREF ,
	--          TrangThaiHopDong ,
	--          IsBanCung ,
	--          CongNo ,
	--          GhiChuHopDong ,
	--          LyDoHuyHopDong ,
	--          DangSuDung ,
	--          IsGiayPhep ,
	--          DmPhongBanREF ,
	--          TenPhongBan ,
	--          DmBoPhanREF ,
	--          TenBoPhan ,
	--          DmNhomLamViecREF ,
	--          TenNhom ,
	--          DmDiaDiemLamViecREF ,
	--          TenDiaDiemLamViec ,
	--          ChuyenTrang ,
	--          CreatedBy ,
	--          CreatedAt ,
	--          LastModifiedBy ,
	--          LastModifiedAt ,
	--          DeletedStatus ,
	--          PrintStatus ,
	--          RecordStatus ,
	--          IsUuDai ,
	--          ThanhTienThucChay ,
	--          ThanhTienHoaDon ,
	--          ThanhTienCongNo ,
	--          ThanhTienThanhToan ,
	--          NgayHuyHopDong ,
	--          NguoiHuyHopDong ,
	--          IsCalcVoucher ,
	--          GiaTriDatCoc ,
	--          TenNhanGoc ,
	--          DmNhanGocREF
	--        )
        SELECT  *
        FROM    #HopDong
    END
	


```
